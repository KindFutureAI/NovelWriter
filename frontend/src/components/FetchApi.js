import React, { Component} from 'react';

class FetchApi extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: [{name: '张三'}, {name: '李四'}, {name: '王五'}]
        };
    }

    // componentDidMount() {
    //     fetch('https://api.example.com/data')
    //         .then(response => response.json())
    //         .then(data => {
    //             this.setState({
    //                 data: data
    //             });
    //         });
    // }

    render() {
        const { data } = this.state;
        const listItems = data.map((item, index) => (
            <li key={index}>
                {item.name}
            </li>
        ));
        return <ul>{listItems}</ul>;
    }
}

export default FetchApi;