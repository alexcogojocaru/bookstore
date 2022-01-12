import logo from './logo.svg';
import './App.css';

import React from 'react';
import BookList from './components/file_component';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      books: []
    };
  }

  componentDidMount() {
    const reqHeaders = new Headers();
    if (reqHeaders.has('Accept')) {
      reqHeaders.set('Accept', 'application/json');
    }
    else {
      reqHeaders.append('Accept', 'application/json');
    }

    const requestParams = {
      method: 'GET',
      headers: reqHeaders
    };

    fetch('http://localhost:8000/api/bookcollection/books', requestParams)
      .then(response => { return response.json(); })
      .then(data => this.setState({'books': data}))
      .catch(console.log);
  }

  render() {
    return (
      <BookList books={this.state.books}/>
    )
  }
}

// function App() {
  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>
  //     </header>
  //   </div>
  // );
// }

export default App;
