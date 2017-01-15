import React, { Component } from 'react';
import { Input, Button, Statistic, Grid } from 'semantic-ui-react';
import axios from 'axios';

import './App.css';

class App extends Component {
  
  constructor(props){
    super(props);
    this.state = {
      tweet: '',
      user: '',
      ans: 0
    }
  }  

  onChangeTweet(e) {
    this.setState({
      tweet: e.target.value
    })
  }

  onChangeUser(e) {
    this.setState({
      user: e.target.value
    })
  }

  onClick() {
    //alert(this.state.user + ': ' + this.state.tweet);
    // Call axios over here and then set state for output

    /*axios.get('/user', {
      params: {
        user: this.state.user,
        tweet: this.state.tweet
      }
    })
    .then(function (response) {
      this.setState({
        ans: response
      })
    })
    .catch(function (error) {
      console.log(error);
    });*/

    this.setState({
      ans: this.state.ans + 1
    });
  }

  render() {
    return (
          <Grid celled='internally' verticalAlign='middle' columns={1} centered style={{paddingTop: 50}}>
            <Grid.Row verticalAlign='middle' centered>
              <Grid.Column>
                <Input
                  style={{padding: 5}}  
                  placeholder="Enter Tweet" 
                  onChange={this.onChangeTweet.bind(this)}
                />

                <Input
                  style={{padding: 5}}   
                  placeholder="Enter Username" 
                  onChange={this.onChangeUser.bind(this)}
                />

                <Button 
                  children="Enter" 
                  onClick={this.onClick.bind(this)}
                />


                <Grid.Row verticalAlign='middle' style={{paddingTop: 50}} centered>
                  <Statistic size={'huge'}>
                    <Statistic.Label>Retweets</Statistic.Label>
                    <Statistic.Value>{this.state.ans}</Statistic.Value>
                  </Statistic>      
                </Grid.Row>
          
              </Grid.Column>
              
            </Grid.Row>
            
          </Grid>
    );
  }
}

export default App;
