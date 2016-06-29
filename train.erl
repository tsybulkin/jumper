%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides RFL training functions
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(train).
-export([train/2, train/4, get_dataset/3
		]).

-define(EPISODE_LEN, 0.5). 
-define(TAU, 0.1).


get_dataset([],_,_) -> ok;
get_dataset([Ae|Targets],N,File) ->
	{ok,Out} = file:open(File, [append]),
	Q = train(Ae,N),
	lists:foreach(
		fun(State)->
			{A,A_der,_} = learn:get_pos(State),
			Ac = learn:get_best_learned_action(State,Q),
			Psi = learn:get_psi(Ac),
			io:format(Out,"~p;~p;~p;~p~n",[Ae,A,A_der,Psi])
		end, dict:fetch_keys(Q)),
	file:close(Out),
	get_dataset(Targets,N,File).


train(Ae,N) -> Q = dict:new(), train(Ae,N,Q,0.2).

train(Ae,0,Q,_) ->
	Pos = phy1:init(1.5),
	Log = run_demo(Ae,Pos,?TAU,?EPISODE_LEN,Q,[]), 
	show1:make_demo(Log,?TAU),
	Q;
train(Ae,N,Q,Eps) ->
	case (N-1) rem 10000 of
		0 -> io:format("Q size: ~p~n",[dict:size(Q)]);
		_ -> ok
	end,
	Init_A = 3*(0.1+random:uniform()),
	Pos = phy1:init(Init_A),
	Q1 = run_episode(Ae,Pos,?TAU,?EPISODE_LEN,Q,Eps),
	train(Ae,N-1,Q1,Eps).


run_episode(Ae,Pos,Tau,T,Q,Eps) when T>0 ->
	State = learn:get_state({_,_,PrevAction}=Pos),
	Action = learn:get_policy(State,Q,Eps),
	Psi = learn:get_psi(Action),
	NextPos = phy1:next_position(Pos,Psi,Tau),
	case phy1:is_pos_out(NextPos) of
		true -> 
			Rwd = -100, 
			learn:learn(State, out_state, Action, Rwd, Q);

		false->
			NextState = learn:get_state(NextPos),
			Rwd = learn:get_reward(Ae,PrevAction,Pos,Action,NextPos),
			Q1 = learn:learn(State, NextState, Action, Rwd, Q),
			run_episode(Ae,NextPos,Tau,T-Tau,Q1,Eps)
	end;
		
run_episode(_Ae,_,_,_T,Q,_) -> Q.




run_demo(Ae,Pos,Tau,T,Q,Log) when T>0 -> 
	State = learn:get_state(Pos),
	Action = learn:get_policy(State,Q,0),
	io:format("~p\t~p~n",[State,Action]),
	Psi = learn:get_psi(Action),
	NextPos = phy1:next_position(Pos,Psi,Tau),
	run_demo(Ae,NextPos,Tau,T-Tau,Q,[Pos|Log]);
run_demo(_,Pos,_,_,_,Log) -> lists:reverse([Pos|Log]).
