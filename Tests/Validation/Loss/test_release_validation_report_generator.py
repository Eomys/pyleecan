from Tests.Validation.Loss.generate_release_validation_reports import (
    BLOCKED,
    FAIL,
    PASS,
    build_case_comparison_conclusion,
    build_leaf_checks,
    build_prius_checks,
    build_overall_comparison_conclusion,
    get_case_report_positioning,
    release_decision,
    status_from_efficiency_band,
)


def _prius_full_summary():
    return {
        "comparison": {
            "geometry_vs_ornl": {
                "airgap_mm": {
                    "reference": 0.73,
                    "model": 0.75,
                    "delta_pct": 2.7,
                }
            },
            "static_vs_published": {
                "reference_power_kW": 50.0,
                "reference_torque_Nm": 400.0,
                "model_power_kW": 54.0,
                "model_torque_Nm": 404.0,
                "power_delta_pct": 8.0,
                "torque_delta_pct": 1.0,
            },
            "efficiency_region_vs_ornl": {
                "ornl_motor_peak_efficiency_band": [0.93, 0.94],
                "model_moderate_region_peak_efficiency": 0.945,
                "model_moderate_region_mean_efficiency": 0.938,
            },
            "drive_cycle_envelope_check": {
                "published_motor_max_speed_rpm": 6000.0,
                "cycle_max_speed_rpm": 4500.0,
                "within_speed_limit": True,
                "published_motor_max_torque_Nm": 400.0,
                "cycle_max_torque_Nm": 360.0,
                "within_torque_limit": True,
            },
        }
    }


def _prius_elmer_summary():
    return {
        "points": [
            {
                "tag": "static_1200_full_load",
                "compare_to_femm": {
                    "torque_delta_pct": -25.0,
                    "power_delta_pct": -25.0,
                },
                "elmer": {"Tem_av_Nm": 350.0, "P_out_W": 44000.0},
                "femm_baseline": {"Tem_av_Nm": 470.0, "P_out_W": 59000.0},
            }
        ]
    }


def _leaf_full_summary():
    return {
        "public_reference": {"peak_torque_Nm": 280.0},
        "drive_cycle": {"summary": {"max_torque_Nm": 250.0}},
        "comparison": {
            "geometry_vs_public": {
                "airgap_mm": {
                    "reference": 0.495,
                    "model": 0.50,
                    "delta_pct": 1.0,
                }
            },
            "power_and_torque_vs_public": {
                "reference_peak_power_kW": 80.0,
                "reference_peak_torque_Nm": 280.0,
                "model_peak_power_kW": 270.0,
                "model_peak_torque_Nm": 375.0,
                "model_power_at_3000_rpm_kW": 125.0,
                "peak_power_delta_pct": 237.5,
                "peak_torque_delta_pct": 33.9,
                "power_at_3000_delta_pct": 56.3,
            },
            "current_voltage_vs_public": {
                "reference_peak_torque_current_arms": 443.0,
                "model_peak_torque_current_arms": 450.0,
                "current_delta_pct": 1.6,
                "reference_voltage_limit_onset_rpm": 4000.0,
                "model_field_weakening_start_rpm": 7000.0,
                "field_weakening_delta_pct": 75.0,
            },
            "efficiency_vs_public": {
                "reference_peak_efficiency": 0.97,
                "model_high_power_peak_efficiency": 0.9596,
            },
            "speed_envelope_vs_public": {
                "reference_max_speed_rpm": 10390.0,
                "model_full_load_max_speed_rpm": 10300.0,
                "drive_cycle_max_speed_rpm": 9800.0,
                "within_drive_cycle_speed_limit": True,
                "within_drive_cycle_torque_limit": True,
            },
            "static_3000rpm_point": {
                "reference_power_kW": 80.0,
                "reference_torque_Nm": 254.6,
                "model_power_kW": 118.0,
                "model_torque_Nm": 375.6,
                "power_delta_pct": 47.5,
                "torque_delta_pct": 47.5,
            },
        },
    }


def _leaf_elmer_summary():
    return {
        "points": [
            {
                "tag": "static_3000_full_load",
                "compare_to_femm": {
                    "torque_delta_pct": 1.2,
                    "power_delta_pct": 1.2,
                },
                "elmer": {"Tem_av_Nm": 379.0, "P_out_W": 119000.0},
                "femm_baseline": {"Tem_av_Nm": 374.0, "P_out_W": 117500.0},
            }
        ]
    }


def test_status_from_efficiency_band_accepts_small_margin():
    assert status_from_efficiency_band(0.947, 0.93, 0.94) == PASS
    assert status_from_efficiency_band(0.955, 0.93, 0.94) == FAIL


def test_build_prius_checks_blocks_large_elmer_gap():
    checks = build_prius_checks(_prius_full_summary(), _prius_elmer_summary())

    elmer_failures = [
        check
        for check in checks
        if check.category == "Elmer vs FEMM" and check.status == FAIL
    ]

    assert len(elmer_failures) == 2
    assert release_decision(checks) == BLOCKED


def test_build_leaf_checks_blocks_public_curve_mismatch():
    checks = build_leaf_checks(_leaf_full_summary(), _leaf_elmer_summary())

    failed_metrics = {check.metric for check in checks if check.status == FAIL}

    assert "peak power [kW]" in failed_metrics
    assert "field-weakening onset [rpm]" in failed_metrics
    assert "static 3000 rpm power [kW]" in failed_metrics
    assert release_decision(checks) == BLOCKED


def test_leaf_report_positioning_is_internal_validation():
    case = {"case_name": "LEAF 2012", "decision": BLOCKED}

    assert get_case_report_positioning("LEAF 2012") == (
        "Internal validation version (内部验证版)"
    )
    conclusion = build_case_comparison_conclusion(case)
    assert "internal validation version (内部验证版)" in conclusion
    assert "not signed against the public power/torque envelope" in conclusion


def test_overall_comparison_conclusion_mentions_leaf_internal_scope():
    payload = {
        "cases": [
            {"case_name": "Prius 2004"},
            {"case_name": "LEAF 2012"},
        ]
    }

    conclusion = build_overall_comparison_conclusion(payload)
    assert "Prius 2004 remains the public signoff case" in conclusion
    assert (
        "LEAF 2012 is reported only as an internal validation version "
        "(内部验证版)" in conclusion
    )
