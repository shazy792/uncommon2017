import React, { Component } from 'react';
import { Input, Button, Statistic, Grid, Image, Header } from 'semantic-ui-react';
import axios from 'axios';

import './App.css';

var config = {
    headers: {'Access-Control-Allow-Origin': 'http://localhost:3000'}
  };

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      tweet: '',
      user: '',
      ans: 0,
      guess: '',
      img: "http://vignette2.wikia.nocookie.net/sawfilms/images/d/da/Iwannaplayagame.jpg/revision/latest?cb=20120227150040"
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

  onChangeGuess(e) {
    this.setState({
      guess: e.target.value
    })
  }

  onClick() {
    //alert(this.state.user + ': ' + this.state.tweet);
    // Call axios over here and then set state for output
    axios.get('http://flask-env.dpumtvmq3q.us-east-2.elasticbeanstalk.com/tweets', {
      params: {
        user: this.state.user,
        tweet: this.state.tweet
      }
    }, config)
    .then((response) => {
      this.setState({
        ans: response.data,
        user: '',
        tweet: '',
        guess: ''
      })
    })
    .catch((error) => {
      console.log(error);
    });

    // if to change img state
    
  }

  onKeyPress(e) {
    if (e.charCode === 13) {
      this.onClick();
    }
  }

  render() {
    return (
          <Grid celled='internally' verticalAlign='middle' columns={1} centered style={{paddingTop: 7}}>
            <Grid.Column>
              <Grid.Row verticalAlign='middle' centered>
                  <Header size='medium' style={{color: 'white'}}>Wanna Play a Game?</Header>
                  <Input
                    value={this.state.tweet}
                    ref='inputTweet'
                    style={{padding: 5}}  
                    placeholder="Enter Tweet" 
                    onChange={this.onChangeTweet.bind(this)}
                  />

                  <Input
                    value={this.state.user}
                    ref='inputUser'
                    style={{padding: 5}}   
                    placeholder="Enter Username" 
                    onChange={this.onChangeUser.bind(this)}
                  />
                </Grid.Row>

                <Grid.Row>
                  <Input
                    value={this.state.guess}
                    ref='inputGuess' 
                    placeholder='Your guess?'
                    style={{paddingRight: 5}}
                    onKeyPress={this.onKeyPress.bind(this)}
                    onChange={this.onChangeGuess.bind(this)}
                  />
                  <Button
                    children="Check!"
                    onClick={this.onClick.bind(this)}
                  />
                </Grid.Row>

                <Grid.Row verticalAlign='middle' style={{paddingTop: 5}} centered>
                  <Statistic style={{color: 'white'}}>
                    <Statistic.Label style={{color: 'white'}}>Retweets</Statistic.Label>
                    <Statistic.Value style={{color: 'white'}}>{this.state.ans}</Statistic.Value>
                  </Statistic>      
                </Grid.Row>

                <Grid.Row verticalAlign='bottom' style={{paddingTop: 5}} centered>
                  <Image src={this.state.img} size='large' centered shape='rounded'/>
                </Grid.Row>
          
              </Grid.Column>
            
          </Grid>
    );
  }
}

export default App;
