import { useEffect } from "react";
import { useState } from "react";
import React, { Component } from 'react';
import { LineChart, Line } from 'recharts';
import { BarChart, Bar, XAxis, YAxis } from 'recharts';
import { Layout,Row, Col, Divider } from 'antd';
const { Header, Footer, Sider, Content } = Layout;

const data = [{name: 'Page A', uv: 400, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 200, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 500, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 200, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 300, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 100, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 350, pv: 2400, amt: 2400}];

const CustomBarChart = (props) => {

	console.log("props data",props.bardata)
	return(
		<>
			<Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
             	<Col className="gutter-row" span={12}>
					<LineChart width={400} height={400} data={data}>
				    	<Line type="monotone" dataKey="uv" stroke="#8884d8" />
				  	</LineChart>
				</Col>
				<Col className="gutter-row" span={12}>
				  	<BarChart width={600} height={300} data={props.bardata}>
					    <XAxis dataKey="testtime"  />
					    <YAxis />
					    <Bar dataKey="activity" barSize={30} fill="#8884d8"
					      />
					 </BarChart>
				</Col>
			</Row>
		</>
	  	)
	}

export default CustomBarChart;