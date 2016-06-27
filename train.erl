%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides RFL training functions
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(train).
-export([train/2, train/4, 
		run_with_pid/0, run_with_pid/5
		]).

-define(EPISODE_LEN, 1.0). 
-define(TAU, 0.01).

train(Ae,N) -> Q = dict:new(), train(Ae,N,Q,0.25).

train(Ae,0,Q,_) ->
	Pos = phy1:init(2.0),
	Log = run_demo(Ae,Pos,?TAU,?EPISODE_LEN,Q,[]), 
	show1:make_demo(Log,?TAU),
	Q;
train(Ae,N,Q,Eps) ->
	case (N-1) rem 10000 of
		0 -> io:format("Q size: ~p~n",[dict:size(Q)]);
		_ -> ok
	end,
	Init_A = 3*(random:uniform()-0.5),
	Pos = phy1:init(Init_A),
	Q1 = run_episode(Ae,Pos,?TAU,?EPISODE_LEN,Q,Eps),
	train(Ae,N-1,Q1,Eps).


run_episode(Ae,Pos,Tau,T,Q,Eps) when T>0 ->
	State = learn:get_state({_,_,PrevAction}=Pos),
	Action = learn:get_policy(State,Q,Eps),
	Psi = learn:get_psi(Action),
	NextPos = phy1:next_position(Pos,Psi,Tau),
	NextState = learn:get_state(NextPos),
	Rwd = learn:get_reward(Ae,PrevAction,State,Action,NextState),
	Q1 = learn:learn(State, NextState, Action, Rwd, Q),
	run_episode(Ae,NextPos,Tau,T-Tau,Q1,Eps);
	
run_episode(_Ae,_Pos,_,_T,Q,_) -> Q.


run_with_pid() -> run_with_pid(0.7,{1.5,0.0,0.0},?TAU,1.0,[]).
	
run_with_pid(Ae,Pos,Tau,T,Log) when T>0 ->
	Cntrl = pid:get_control(Ae,Pos),
	io:format("\tControl:~p",[Cntrl]),
	Psi = pid:get_psi(Cntrl), io:format("\tPsi:~p~n",[Psi]),
	NextPos = phy1:next_position(Pos,Psi,Tau),
	io:format("\Pos:~p",[NextPos]),
	run_with_pid(Ae,NextPos,Tau,T-Tau,[NextPos|Log]);
run_with_pid(_,_,Tau,_,Log) -> 
	io:format("~p~n",[lists:reverse(Log)]),
	show1:make_demo(lists:reverse(Log), Tau).



run_demo(Ae,Pos,Tau,T,Q,Log) when T>0 -> 
	State = learn:get_state(Pos),
	Action = learn:get_policy(State,Q,0),
	io:format("~p\t~p~n",[State,Action]),
	Psi = learn:get_psi(Action),
	NextPos = phy1:next_position(Pos,Psi,Tau),
	run_demo(Ae,NextPos,Tau,T-Tau,Q,[NextPos|Log]);
run_demo(_,_,_,_,_,Log) -> lists:reverse(Log).
