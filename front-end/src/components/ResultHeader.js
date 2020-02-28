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
                        <th>Term</th>
                        <th>Area of Study</th>
                        <th>CIE</th>
                        <th>RO</th>
                        <th>IO</th>
                        <th>Website</th>
                    </tr>
                </table>
            </div>
        );
    }
}

export default ResultHeader;