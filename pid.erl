%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides PID controller
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(pid).
-export([get_control/2, get_psi/1
		]).

-define(Kp, 1.0).
-define(Kd, 1.0).
-define(Ki, 0.0).


get_control(Ae,{A,A_der,_}) -> ?Kp*(Ae-A) + ?Kd*A_der.


get_psi(E) ->
	case E>0 of
		true -> max(-0.4,-E/2);
		false-> min(0.8, -E)
	end.