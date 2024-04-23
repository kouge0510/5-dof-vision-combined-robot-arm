clear;
close all;
clc;
clear L;
angle=pi/180; %角度转换
L1 = 110; L2 = 105; L3 = 75; L4 = 190;
%D-H参数表
theta1 = 0; D1 = 0; A1 = 0; alpha1 = 0; 
theta2 = 0; D2 = 0; A2 = 0; alpha2 = pi/2; 
theta3 = 0; D3 = 0; A3 = L1; alpha3 = 0; 
theta4 = 0; D4 = 0; A4 = L2; alpha4 = 0; 
theta5 = 0; D5 = 0; A5 = L3; alpha5 =0; 
%% DH法建立模型,关节转角，关节距离，连杆长度，连杆转角，关节类型（0转动，1移动）,关节范围
L(1) = Link([theta1, D1, A1, alpha1, 0], 'modified');L(1).qlim =[-180*angle, 180*angle];
L(2) = Link([theta2, D2, A2, alpha2, 0], 'modified');L(2).qlim =[-180*angle, 180*angle];
L(3) = Link([theta3, D3, A3, alpha3, 0], 'modified');L(3).qlim =[-180*angle, 180*angle];
L(4) = Link([theta4, D4, A4, alpha4, 0], 'modified');L(4).qlim =[-180*angle, 180*angle];
L(5) = Link([theta5, D5, A5, alpha5, 0], 'modified');L(5).qlim =[-180*angle, 180*angle];
%% 显示机械臂
robot0 = SerialLink(L,'name','five');
theta = [90 60 90 90 90]*angle; %初始关节角度
figure(1)
robot0.plot(theta);
robot0.teach
title('五轴机械臂模型');
%% 运动学计算
T = robot0.fkine(theta).T %运动学正解
t = robot0.fkine(theta, L1, L2, L3, L4)
theta_ikine = DOF5_ikine(T, L1, L2, L3, L4)%逆解