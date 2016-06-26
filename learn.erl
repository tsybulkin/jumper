%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides RF learning functions
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(learn).
-export([get_state/2, get_policy/2
		]).

-define(EPS,   0.1).
-define(ALPHA, 0.8).
-define(GAMA,  0.95).


get_state(Ae,{A,A_der,_Psi}) -> {round(10*(Ae - A)), round(10*A_der)}. 


learn(State, NextState, Action, Reward, Q) -> 
	case dict:find(State,Q) of
		{ok, Values} -> case lists:keyfind(Action,2,Values) of
							{V,Action} -> V;
							false -> V = 0
						end;
		error ->
			Values = [{0,Action}], V = 0
	end,
	V1 = get_state_value(NextState,Q),
	V_new = V + ?ALPHA * (Reward + ?GAMA * V1 - V),
	Values1 = lists:keyreplace(Action,2,Values,{V_new,Action}),
	dict:store(Action,Values1,Q).



get_state_value(State,Q) ->
	case dict:find(State,Q) of
		{ok, Values} -> {V,_} = lists:max(Values), V;
		error -> 0
	end.


get_best_learned_action(State,Q) -> 
	case dict:find(State,Q) of
		{ok, Values} -> {_,A} = lists:max(Values), A;
		error -> get_random_action()
	end.


get_policy(State,Q) ->
	case flip_coin(0.1) of
		true -> get_random_action();
		false-> get_best_learned_action(State,Q)
	end.


get_random_action() -> random:uniform(15)-5. 


get_psi(Action) -> Action/10.


flip_coin(P) -> random:uniform() < P.

