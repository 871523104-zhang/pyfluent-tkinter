#include "udf.h"
DEFINE_PROPERTY(viscosity,c,t)
{   
	real mu = 0.0;/*�����ܶ�ǧ��ÿ�����ף�ճ��Ϊ����ѧճ��Pa��s*/
	real temp = C_T(c,t); /*�õ�������thread�ϵ�ÿһ��cell���¶�,��λΪK*/
	mu = 0.0663*exp(-0.023*temp);/*���㶯��ѧճ��*/
	return mu;/*����ճ��ֵ*/
}