import React, { Component } from 'react'
import { Table } from 'reactstrap'

class SearchResults extends Component {
    constructor(props) {
        super(props);
        console.log('props: ' + this.props.filteredPrograms);
    }
    componentDidMount() {

    }
    render() {
        // Make a table of programs and store it
        let filteredPrograms = this.props.state.filteredProgramList.map((program) => {
            return (
                <tr key={program.id}>
                    <td>{program.id}</td>
                    <td>{program.country}</td>
                    <td>{program.term}</td>
                    <td>{program.name}</td>
                    <td>{program.language}</td>
                    <td>{program.cost}</td>
                    {console.log(program.website)}
                    <a href={program.website} target="_blank"><td>{program.website}</td></a>
                </tr>
            )

        });
        return (
            <div className="result">
                <Table>
                    <thead>
                        <tr>
                            <th>id</th>
                            <th>Country</th>
                            <th>Term</th>
                            <th>Name</th>
                            <th>Language</th>
                            <th>Cost</th>
                            <th>Website</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filteredPrograms}
                    </tbody>
                </Table>
            </div>
        )
    }
}

export default SearchResults;
