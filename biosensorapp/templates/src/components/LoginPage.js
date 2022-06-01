import React, { Component } from 'react';
import { Form, Input, Button, Checkbox } from 'antd';
import axios from 'axios';
//import { Router, browserHistory } from 'react-router'
import { withRouter } from "react-router";
import { useNavigate } from 'react-router-dom';
import * as Constants from '../constants/AppConstants'
import {toast} from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import 'antd/dist/antd.css';
import '../App.css'


const LoginPage = (props) => {


	// for the navigation
	const navigate = useNavigate();

	// for checking if user is already logged in

	//api call to get the users from data
  useEffect(() => {
    let data ;  
    axios.get('http://'+Constants.API_URL+'/bio/check-session/')
    .then(res => {
        data = res.data;
        if(data)
        {
          
        }
    })
    .catch(err => {})
  
	}, []);

	

  const onFinish = (values) => {
	    console.log('Success:', values);    
	    let data ;
	    //calling api to veirfy the user details
	    axios.post('http://'+Constants.API_URL+'/bio/user-login/',{'user_email':values.username,
	    	'user_pass':values.password})
	    .then(res => {
	        data = res.data;
	        if(data)
	        {          
	        	//navigating to home page after successful login
	        
	         navigate("/home");
	         
	        }
	    })
	    .catch(err => {})
  };

  const onFinishFailed = (errorInfo) => {
    	console.log('Failed:', errorInfo);
  };


return(
		<Form
					className = 'form-body'
		      name="basic"
		      
		      initialValues={{
		        remember: true,
		      }}
		      onFinish={onFinish}
		      onFinishFailed={onFinishFailed}
		      autoComplete="off"
		    >
		      <Form.Item
		        
		        name="username"
		        className = 'form-elem'
		        rules={[
		          {
		            required: true,
		            message: 'Please input your username!',
		          },
		        ]}
		      >
		        <Input placeholder = "Enter Email" />
		      </Form.Item>

		      <Form.Item
		        
		        name="password"
		        className = 'form-elem'
		        rules={[
		          {
		            required: true,
		            message: 'Please input your password!',
		          },
		        ]}
		      >
		        <Input.Password  placeholder = "Enter Password" />
		      </Form.Item>

		    

		      <Form.Item >
		        <Button  className = "form-button" type="primary" htmlType="submit">
		          Login
		        </Button>
		      </Form.Item>
		    </Form>
		)

	};

export default LoginPage;