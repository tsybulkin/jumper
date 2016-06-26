%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides RFL training functions
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(train).
-export([train/1, train/2
		]).

-define(EPISODE_LEN, 1.0). 
-define(TAU, 0.01).

train(N) -> Q = dict:new(), train(N,Q).

train(0,Q) ->
	Pos = phy1:init(2.0),
	Target = 0.5,
	Log = run_demo(Target,Pos,?TAU,?EPISODE_LEN,Q,[]), 
	show1:make_demo(Log,?TAU),
	Q;
train(N,Q) ->
	Init_A = 3*(random:uniform()-0.5),
	Pos = phy1:init(Init_A),
	Target = 3*(random:uniform()-0.5),
	Q1 = run_episode(Target,Pos,?TAU,?EPISODE_LEN,Q),
	train(N-1,Q1).


run_episode(Ae,Pos,Tau,T,Q) when T>0 ->
	State = learn:get_state(Ae,Pos),
	Action = learn:get_policy(State,Q),
	Psi = learn:get_psi(Action),
	NextPos = phy1:next_position(Pos,Psi,Tau),
	NextState = learn:get_state(Ae,NextPos),
	Rwd = learn:get_reward(State,Action,NextState),
	Q1 = learn:learn(State, NextState, Action, Rwd, Q),

	case learn:is_terminal_state(NextState) of
		true -> Q1;
		false-> run_episode(Ae,NextPos,Tau,T-Tau,Q1)
	end;
run_episode(Ae,Pos,_,T,Q) ->
	State = learn:get_state(Ae,Pos),
	V = learn:get_state_value(State,Q),
	{A,_,_} = Pos,
	io:format("end of the episode.T=~ps. Final error: ~p. Terminal state value: ~p~n",[T,Ae-A,V]),
	Q.


run_demo(Ae,Pos,Tau,T,Q,Log) when T>0 -> 
	State = learn:get_state(Ae,Pos),
	Action = learn:get_policy(State,Q),
	Psi = learn:get_psi(Action),
	NextPos = phy1:next_position(Pos,Psi,Tau),
	NextState = learn:get_state(Ae,NextPos),
	case learn:is_terminal_state(NextState) of
		true -> lists:reverse([NextPos|Log]);
		false-> run_demo(Ae,NextPos,Tau,T-Tau,Q,[NextPos|Log])
	end;
run_demo(_,_,_,_,_,Log) -> lists:reverse(Log).
