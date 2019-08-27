path_txt = "my_path_txt" ;
idmatlab = my_id_matlab ;

mo_smooth("off"); 
nelm=mo_numelements();
nnod=mo_numnodes();

fp1=openfile(path_txt .. "nodes" .. tostring(idmatlab) .. ".txt","w")

for k=1,nnod do
    x,y=mo_getnode(k);	
    write(fp1,x," ",y,"\n");
end

closefile(fp1);

fp2=openfile(path_txt .. "elements" .. tostring(idmatlab) .. ".txt","w")
fp3=openfile(path_txt .. "results" .. tostring(idmatlab) .. ".txt","w")

for k=1,nelm do
	p1,p2,p3,cx,cy,s,grp=mo_getelement(k);
	a,bx,by,o,nrg,hx,hy,Je,Js,mux,muy=mo_getpointvalues(cx,cy);	
	write(fp2,p1," ",p2," ",p3," ",cx," ",cy," ",s," ",grp,"\n");
	write(fp3,bx," ",by," ",hx," ",hy," ",mux,"\n");
end

closefile(fp2);
closefile(fp3);