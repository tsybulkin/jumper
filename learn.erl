%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides RF learning functions
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(learn).
-export([get_state/2, get_policy/2,get_state_value/2,
		is_terminal_state/1,
		get_reward/3,
		learn/5,
		get_psi/1
		]).

-define(EPS,   0.1).
-define(ALPHA, 0.8).
-define(GAMA,  0.95).



get_state(Ae,{A,A_der,_Psi}) -> {round(10*(Ae - A)), round(10*A_der)}. 


get_reward(_State,_Action,{A,A1}) ->
	case is_terminal_state({A,A1}) of
		true -> 10/(abs(A)+1) - abs(A1);
		false ->
			if
				A < -30 -> -10;
				A > 30  -> -10;
				A == 0 andalso A1 == 0 -> 100;
				true -> -abs(A)/10 - abs(A1)/20
			end
	end.


is_terminal_state({0,0}) -> true;
is_terminal_state(_) -> false.



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
			if V>0 -> A; length(Values)>100 -> A; true -> get_random_action() end;
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

