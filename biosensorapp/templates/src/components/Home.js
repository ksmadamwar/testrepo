import { useEffect } from "react";
import { useState } from "react";
import React, { Component } from 'react';
import CustomBarChart from '../charts/BarCharts';
import axios from 'axios';
import { Layout,Row, Col, Divider } from 'antd';
//import Constants from '../constants/AppConstants'
const { Header, Footer, Sider, Content } = Layout;



const Home = () => {
  const [uid,setid] = useState(1);
  const [barData,setBarData] = useState(1);

  //api call to get the users from data
  useEffect(() => {
    let data ;
    const headers = {
        'Content-Type': 'application/json'
    }
    axios.get('http://192.168.56.1:8000/bio/get-users/')
    .then(res => {
        data = res.data;
        if(data)
        {
          setid(data['data'][0]['user_id']) 
        }
    })
    .catch(err => {})
  
}, []);

//called when user clicks on submit button

const handleUserSelect = () =>
{
  //calling an api to get sensor data for the selected user
  let data ;
  const headers = {
        'Content-Type': 'application/json'
    }
    axios.post('http://192.168.56.1:8000/bio/get-sensor-data/',{'uid':uid})
    .then(res => {
        data = res.data;
        if(data)
        {
          
         setBarData(data['sensor-data'])
        }
    })
    .catch(err => {})
}  

  return (
  
  <Layout>
    <header>
       <Divider orientation="left">
          <h1>Hello {uid}</h1>
        </Divider>
    </header>
    <Content>
        <Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
             <Col className="gutter-row" span={24}>
               <button onClick={handleUserSelect} type="submit">
                    Submit
                </button>
              </Col>
        </Row>
        <Row gutter={{ xs: 8, sm: 16, md: 24, lg: 32 }}>
             <Col className="gutter-row" span={24}>
                <CustomBarChart bardata = {barData}/>
              </Col>
        </Row>
    </Content>
  </Layout>
  
  );

};

export default Home;

