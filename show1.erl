%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module contains funs for showing simulation
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(show1).
-export([make_demo/2
		]).
-define(PI,3.1416).
-define(Xt, 0.2).
-define(Yt, 0.2).

make_demo([{A,_,_}|Log],Tau) ->
	{ok,Out} = file:open("muscle.html", [write]),
	io:format(Out, "<html>~n<body>
		<svg width='1000' height='650'>~n",[]),

	{Xt1,Yt1}=px({?Xt,?Yt}),
	io:format(Out, "\t<rect x='~w' y='~w' width='100' height='400'
    				style='fill:grey;stroke:brown;'/>~n~n",[Xt1,Yt1-200]),
	{Xm,Ym} = phy1:get_XYm(?Xt,?Yt,A), {Xm1,Ym1} = px({Xm,Ym}),
	io:format(Out, "\t<line x1='~w' y1='~w' x2='~w' y2='~w'
		style='stroke:red;stroke-width:3' >~n",[Xm1,Ym1,Xt1,Yt1]),

	make_demo(Log,Xt1,Yt1,0,Tau,Out).

make_demo([{A,_,Psi}|Log],Xt1,Yt1,T,Tau,Out) ->	
	{Xm,Ym} = phy1:get_XYm(?Xt,?Yt,A), {Xm1,Ym1} = px({Xm,Ym}),
	%{X1,Y1,X2,Y2} = phy1:get_servo(Xm,Ym,A,Psi), 
	%{Xs1,Ys1} = px({X1,Y1}), {Xs2,Ys2} = px({X2,Y2}),
	
	io:format(Out,"
		<set attributeName='x1' attributeType='XML'
         to='~w' begin='~ws'  />~n",[Xm1,T]),
	io:format(Out,"
		<set attributeName='y1' attributeType='XML'
         to='~w' begin='~ws'  />~n",[Ym1,T]),
	
	make_demo(Log,Xt1,Yt1,T+Tau,Tau,Out);
make_demo([],_,_,_,_,Out) ->	
	io:format(Out, "<line/>~n</svg>\n</body>~n</html>",[]),
	file:close(Out).


px({X,Y}) -> {100+round(X*1500), 600-round(Y*1500)}.

degr(Rad) -> round(180*Rad/?PI).
