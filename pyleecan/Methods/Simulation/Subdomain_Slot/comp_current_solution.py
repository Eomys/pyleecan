def comp_current_solution(self):
    """Method description

    Parameters
    ----------
    self: Subdomain_SlotCW
        a Subdomain_SlotCW object

    Returns
    ----------
    var: type
        var description
    """

    # if is_AW %airgap winding
    #     X_r = mu0*(-f(v, Rso).*E_nrR(v, r, Ry) - f(v, Ry).*E_nrR(v, Rso, r) + f(v, r).*E_nrR(v, Rso, Ry))./E_nrR(v, Rso, Ry) ; %particular function
    #     dX_r = mu0*(-v.*f(v, Rso).*P_nrR(v, r, Ry)./r + v.*f(v, Ry).*P_nrR(v, Rso, r)./r + g(v, r).*E_nrR(v, Rso, Ry))./E_nrR(v, Rso, Ry) ;  %derivative of the particular function
    #     Xv_r = 0 ;
    #     dXv_r = 0 ;
    # else %slotted winding
    #     if is_SDM_linear_stator == 2
    #         X_r = mu0*(-r.^2/2 + Ry^2.*log(r))/2 ; %constant particular function
    #         dX_r = mu0*(-r.^2 + Ry^2)./(2*r) ;  %derivative of the constant particular function
    #     else
    #         X_r = -mu0*r.^2/4  ; %constant particular function
    #         dX_r = -mu0*r/2 ;  %derivative of the constant particular function
    #     end
    #     if Nlay_tan1==2
    #         %Lubin reformulation
    #         e_v = v*pi/d ;
    #         if is_openingS == 1 % if there are stator slot openings
    #             Xv_r =  mu0*(-Rso.*g(e_v, Rso).*P_nrR(e_v, r, Ry)./(e_v.*E_nrR(e_v, Rso, Ry)) + Ry.*g(e_v, Ry).*P_nrR(e_v, Rso, r)./(e_v.*E_nrR(e_v, Rso, Ry)) + f(e_v, r)) ; %harmonic particular function
    #             dXv_r = mu0*(-Rso.*g(e_v, Rso).*E_nrR(e_v, r, Ry)./(r.*E_nrR(e_v, Rso, Ry)) - Ry.*g(e_v, Ry).*E_nrR(e_v, Rso, r)./(r.*E_nrR(e_v, Rso, Ry)) + g(e_v, r)) ;   %derivative of the harmonic particular function
    #         else
    #             Xv_r =  mu0*( Ry.*g(e_v, Ry).*E_nrR(e_v, Rso, r)./(e_v.*P_nrR(e_v, Rso, Ry)) - f(e_v, Rso).*P_nrR(e_v, r, Ry)./P_nrR(e_v, Rso, Ry) + f(e_v, r) ) ; %harmonic particular function
    #             dXv_r = mu0*(-Ry.*g(e_v, Ry).*P_nrR(e_v, Rso, r)./(r.*P_nrR(e_v, Rso, Ry)) - e_v.*f(e_v, Rso).*E_nrR(e_v, r, Ry)./(r.*P_nrR(e_v, Rso, Ry)) + g(e_v, r) ) ;   %derivative of the harmonic particular function
    #         end
    #     else
    #         Xv_r = 0 ; %zeros(size(v)) ;
    #         dXv_r = 0 ; %zeros(size(v)) ;
    #     end
    # end

    # function result = f(v,r)
    #     result = r.^2./(v.^2-4) ;
    #     if length(r) == 1
    #         result(v==2) = -r.^2.*(-log(r)+1/4)/4 ;
    #     else
    #         result(v==2) = -r(v==2).^2.*(-log(r(v==2))+1/4)/4 ;
    #     end
    # end

    # function result = g(v,r)
    #     result = 2*r./(v.^2-4) ;
    #     if length(r) == 1
    #         result(v==2) = r.*(-log(r)+1/4)/2 - r/4 ;
    #     else
    #         result(v==2) = r(v==2).*(-log(r(v==2))+1/4)/2 - r(v==2)/4 ;
    #     end
    # end

    return var
