import React, { Component } from 'react';

class ResultHeader extends Component {
    render() {
        return (
            <div className="result-header">
                <table>
                    <tr>
                        <th>Country</th>
                        <th>Program Name</th>
                        <th>Language</th>
                    </tr>
                </table>
            </div>
        );
    }
}

export default ResultHeader;