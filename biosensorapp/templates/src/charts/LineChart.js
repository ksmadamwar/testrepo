import { useEffect } from "react";
import { useState } from "react";
import React, { Component } from 'react';
import { LineChart, Line } from 'recharts';
import { Layout,Row, Col, Divider } from 'antd';


const data = [{name: 'Page A', uv: 400, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 200, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 500, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 200, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 300, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 100, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 350, pv: 2400, amt: 2400}];

const CustomLineChart = (props) => {
	return(
		<>
			<Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
             	<Col className="gutter-row" span={12}>
					<LineChart width={400} height={400} data={data}>
				    	<Line type="monotone" dataKey="uv" stroke="#8884d8" />
				  	</LineChart>
				</Col>
				
			</Row>
		</>
	  	)
	}

export default CustomLineChart;