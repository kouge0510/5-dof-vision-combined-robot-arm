function theta_ikine = DOF5_ikine(oT, ol1, ol2, ol3, ol4)
%5自由度逆解运算
l1 = ol1; l2 = ol2; l3 = ol3; l4 = ol4;
r11 = oT(1, 1);r12 = oT(1, 2);r13 = oT(1, 3);px = oT(1, 4);
r21 = oT(2, 1);r22 = oT(2, 2);r23 = oT(2, 3);py = oT(2, 4);
r31 = oT(3, 1);r32 = oT(3, 2);r33 = oT(3, 3);pz = oT(3, 4);
% theta1 两个解
theta1_1 = atan2(py, px) - atan2(0, (px^2 + py^2)^0.5);
%theta1_2 = atan2(py, px) - atan2(0, -(px^2 + py^2)^0.5);
s1 = sin(theta1_1);
c1 = cos(theta1_1);
% theta3 两个解
c3 = ((px*c1)^2 + 2*px*py*s1*c1 + (py*s1)^2 + pz^2 - l2^2 - l3^2) / (2*l2*l3);
theta3_1 = atan2(sqrt(1-c3^2), c3);
theta3_2 = atan2(-sqrt(1-c3^2), c3);
s3_1 = sin(theta3_1);
s3_2 = sin(theta3_2);
% theta2 两个解
s2_1 = (pz*(c3*l3+l2)+s3_1*l3*(c1*px+s1*py))/(-(c3*l3+l2)^2-(s3_1*l3)^2);
s2_2 = (pz*(c3*l3+l2)+s3_2*l3*(c1*px+s1*py))/(-(c3*l3+l2)^2-(s3_2*l3)^2);
c2_1 = ((c1*px+s1*py)+s2_1*s3_1*l3)/(c3*l3+l2);
c2_2 = ((c1*px+s1*py)+s2_2*s3_2*l3)/(c3*l3+l2);
theta2_1 = atan2(s2_1, c2_1);
theta2_2 = atan2(s2_2, c2_2);
% theta5 一个解
theta5 = atan2(s1*r11-c1*r21, s1*r12-c1*r22);
% theta4 四个解
theta4_1_1 = atan2(s2_1*c3+c2_1*s3_1, s2_1*s3_1-c2_1*c3) + atan2(sqrt((s2_1*s3_1-c2_1*c3)^2+(s2_1*c3+c2_1*s3_1)^2-r33^2), r33);
theta4_1_2 = atan2(s2_1*c3+c2_1*s3_1, s2_1*s3_1-c2_1*c3) - atan2(sqrt((s2_1*s3_1-c2_1*c3)^2+(s2_1*c3+c2_1*s3_1)^2-r33^2), r33);
theta4_2_1 = atan2(s2_2*c3+c2_2*s3_2, s2_2*s3_2-c2_2*c3) + atan2(sqrt((s2_2*s3_2-c2_2*c3)^2+(s2_2*c3+c2_2*s3_2)^2-r33^2), r33);
theta4_2_2 = atan2(s2_2*c3+c2_2*s3_2, s2_2*s3_2-c2_2*c3) - atan2(sqrt((s2_2*s3_2-c2_2*c3)^2+(s2_2*c3+c2_2*s3_2)^2-r33^2), r33);
theta_ikine = [theta1_1 theta2_1 theta3_1 theta4_1_1 theta5;
theta1_1 theta2_1 theta3_1 theta4_1_2 theta5;
theta1_1 theta2_2 theta3_2 theta4_2_1 theta5;
theta1_1 theta2_2 theta3_2 theta4_2_2 theta5];
end