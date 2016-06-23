%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module contains funs for showing simulation
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(show).
-export([make_demo/1
		]).
-define(PI,3.1416).

make_demo([{A,_,B,_,_}|Log]) ->
	{ok,Out} = file:open("jumper.html", [write]),
	Xt = 0.05, Yt = 0,
	{Xt1,Yt1}=px({Xt,Yt}),
	{Xa,Ya} = px(phy:get_XYa(Xt,Yt,B)),
	{Xh,Yh} = px(phy:get_XYh(Xt,Yt,B)),
	{X0,Y0} = px(phy:get_XY0(Xt,Yt,A,B)),
	{X1,Y1} = px(phy:get_XY1(Xt,Yt,B)),
	Rx = round(1.2*math:sqrt((X0-Xh)*(X0-Xh)+(Y0-Yh)*(Y0-Yh))),
	Ry = Rx div 2,

	io:format(Out, "<svg width='1000' height='700'>~n",[]),

	io:format(Out,"\t<ellipse cx='~w' cy='~w' rx='~w' ry='~w' 
					style='fill:lime;stroke:purple;stroke-width:1' 
					transform='rotate(~w ~w ~w)'/>~n",[X0,Y0,Rx,Ry,degr(?PI/2-A-B),X0,Y0]),
	io:format(Out,"\t<polygon points='~w,~w ~w,~w ~w,~w ~w,~w' 
					style='fill:lime;stroke:purple;stroke-width:1' />~n",[Xt1,Yt1,Xa,Ya,Xh,Yh,X1,Y1]),
	
	io:format(Out, "</svg>\n",[]),
	file:close(Out).


px({X,Y}) -> {100+round(X*4000), 600-round(Y*4000)}.

degr(Rad) -> round(180*Rad/?PI).
