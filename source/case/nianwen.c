#include "udf.h"
DEFINE_PROPERTY(viscosity,c,t)
{   
	real mu = 0.0;/*定义密度千克每立方米，粘度为动力学粘度Pa·s*/
	real temp = C_T(c,t); /*得到流体域thread上的每一个cell的温度,单位为K*/
	mu = 0.0663*exp(-0.023*temp);/*计算动力学粘度*/
	return mu;/*返回粘度值*/
}