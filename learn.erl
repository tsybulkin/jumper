%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides RF learning functions
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(learn).
-export([get_state/2
		]).


get_state(Ae,{A,A_der,Psi}) -> {round(10*(Ae - A)), round(10*A_der)}. 