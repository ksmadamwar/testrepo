import { useEffect } from "react";
import { useState } from "react";
import React, { Component } from 'react';
import { LineChart, Line } from 'recharts';
import { BarChart, Bar, XAxis, YAxis } from 'recharts';
import { Layout,Row, Col, Divider } from 'antd';
const { Header, Footer, Sider, Content } = Layout;

const CustomBarChart = (props) => {

	console.log("props data",props.bardata)
	return(
		<>
			<Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
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