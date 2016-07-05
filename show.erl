%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module contains funs for showing simulation
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(show).
-export([make_demo/2
		]).
-define(PI,3.1416).
-define(Xt, 0.05).
-define(Yt, 0).

make_demo(Log,Tau) ->
	{ok,Out} = file:open("jumper.html", [write]),
	io:format(Out, "<svg width='1000' height='650'>~n",[]),
	
	io:format(Out,"~n<polygon points='~w,~w ~w,~w ~w,~w ~w,~w' 
					style='fill:brown;stroke:purple;stroke-width:1' >~n",[0,0,0,0,0,0,0,0]),
	draw_leg(Log,0,Tau,Out),

	io:format(Out,"\t<line x1='~w' y1='~w' x2='~w' y2='~w' 
					style='fill:brown;stroke:purple;stroke-width:15' >~n",[0,0,0,0]),
	draw_body(Log,0,Tau,Out),
	io:format(Out, "</svg>\n",[]),
	file:close(Out).


draw_leg([{_,_,B,_,_}|Log],T,Tau,Out) ->
	{Xt1,Yt1}=px({?Xt,?Yt}),
	{Xa,Ya} = px(phy:get_XYa(?Xt,?Yt,B)),
	{Xh,Yh} = px(phy:get_XYh(?Xt,?Yt,B)),
	{X1,Y1} = px(phy:get_XY1(?Xt,?Yt,B)),
	io:format(Out,"\t<set attributeName='points' attributeType='XML'
		to='~w,~w ~w,~w ~w,~w ~w,~w' begin='~ws'  />~n",
         	[Xt1,Yt1,Xa,Ya,Xh,Yh,X1,Y1,T]),
	draw_leg(Log,T+Tau,Tau,Out);
draw_leg([],_,_,Out) ->
	io:format(Out,"</polygon>~n",[]).


draw_body([{A,_,B,_,_}|Log],T,Tau,Out) ->
	{X1,Y1} = px(phy:get_XYh(?Xt,?Yt,B)),
	{X2,Y2} = px(phy:get_XY2(?Xt,?Yt,A,B)),
	
	io:format(Out,"<set attributeName='x1' attributeType='XML'
		to='~w' begin='~w'  />~n",[X1,T]),
	io:format(Out,"<set attributeName='y1' attributeType='XML'
		to='~w' begin='~w'  />~n",[Y1,T]),
	io:format(Out,"<set attributeName='x2' attributeType='XML'
		to='~w' begin='~w'  />~n",[X2,T]),
	io:format(Out,"<set attributeName='y2' attributeType='XML'
		to='~w' begin='~w'  />~n",[Y2,T]),
		
	draw_body(Log,T+Tau,Tau,Out);
draw_body([],_,_,Out) ->
	io:format(Out,"</line>~n",[]).




px({X,Y}) -> {300+round(X*2000), 400-round(Y*2000)}.

degr(Rad) -> round(180*Rad/?PI).
