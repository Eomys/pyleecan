path_txt = "my_path_txt" ;
idmatlab = my_id_matlab ;

mo_smooth("off");
nelm=mo_numelements();

fp=openfile(path_txt .. "results" .. tostring(idmatlab) .. ".txt","w")

for k=1,nelm do
	p1,p2,p3,cx,cy=mo_getelement(k);
	a,bx,by,o,nrg,hx,hy,Je,Js,mux,muy=mo_getpointvalues(cx,cy);		
	write(fp,bx," ",by," ",hx," ",hy," ",mux,"\n");
end

closefile(fp);