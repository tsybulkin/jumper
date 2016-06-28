%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides RF learning functions
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(learn).
-export([get_state/1, get_policy/3,get_state_value/2,
		%is_terminal_state/1,
		get_reward/5,
		learn/5,
		get_psi/1
		]).

-define(ALPHA, 0.5).
-define(GAMA,  0.95).



get_state({A,A_der,_Psi}) -> {round(10*A), round(5*A_der)}. 


get_reward(Ae,PrevAction,{_A1,_Ad1,_},Action,{A2,_Ad2,_}) ->
	if
		A2 < 0 -> -50;
		A2 > 30  -> -50;
		true -> -1 + 1/(abs(Ae-A2)+0.1) - abs(PrevAction-Action)*0
	end.



learn(State, NextState, Action, Reward, Q) -> 
	V1 = get_state_value(NextState,Q),
	case dict:find(State,Q) of
		{ok, Values} -> 
			%io:format("Values: ~p\t",[Values]),
			case lists:keyfind(Action,2,Values) of
				{V,Action} -> 
					V_new = (1-?ALPHA)*V + ?ALPHA * (Reward + ?GAMA * V1),
					Values1 = lists:keyreplace(Action,2,Values,{V_new,Action});
				false -> 
					Values1 = [{V1,Action}|Values]
			end;
		error ->
			Values1 = [{V1,Action}]
	end,
	%io:format("New values for ~p: ~p~n",[State,Values1]),
	dict:store(State,Values1,Q).



get_state_value(State,Q) ->
	case dict:find(State,Q) of
		{ok, Values} -> {V,_} = lists:max(Values), V;
		error -> 0
	end.


get_best_learned_action(State,Q) -> 
	case dict:find(State,Q) of
		{ok, Values} -> 
			{V,A} = lists:max(Values), 
			if V>0 -> A; length(Values)>5 -> A; true -> get_random_action([Ac || {_,Ac}<-Values]) end;
		error -> get_random_action()
	end.


get_policy(State,Q,Eps) ->
	case flip_coin(Eps) of
		true -> get_random_action();
		false-> get_best_learned_action(State,Q)
	end.


get_random_action() -> random:uniform(15)-5. 

get_random_action(Ls) ->
	A = random:uniform(15)-5,
	case lists:member(A,Ls) of
		true -> get_random_action(Ls);
		false -> A
	end.


get_psi(Action) -> Action/10.


flip_coin(P) -> random:uniform() < P.

