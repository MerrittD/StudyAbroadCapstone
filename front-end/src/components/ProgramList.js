import React, { Component } from 'react'

export default class ProgramList extends Component {
    render() {
        return (

            <div className="result">
                <table>
                    <tr>
                        <td><input type="checkbox" name="name1" />&nbsp;</td>
                        <td>0001</td>
                        <td className="result-country">Exchange Program Name</td>
                        <td className="result-prog-name">Australia</td>
                        <td>Fall</td>
                        <td>English</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="name1" />&nbsp;</td>
                        <td>0002</td>
                        <td className="result-country">Exchange Program Name</td>
                        <td className="result-prog-name">Brazil</td>
                        <td>Summer</td>
                        <td>Portuguese</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="name1" />&nbsp;</td>
                        <td>0003</td>
                        <td className="result-country">Exchange Program Name</td>
                        <td className="result-prog-name">China</td>
                        <td>Spring</td>
                        <td>English</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="name1" />&nbsp;</td>
                        <td>0004</td>
                        <td className="result-country">Exchange Program Name</td>
                        <td className="result-prog-name">England</td>
                        <td>Fall</td>
                        <td>English</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="name1" />&nbsp;</td>
                        <td>0005</td>
                        <td className="result-country">Exchange Program Name</td>
                        <td className="result-prog-name">Italy</td>
                        <td>Spring</td>
                        <td>Italian</td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" name="name1" />&nbsp;</td>
                        <td>0006</td>
                        <td className="result-country">Exchange Program Name</td>
                        <td className="result-prog-name">Spain</td>
                        <td>Summer</td>
                        <td>Spanish</td>
                    </tr>
                </table>
            </div>

        )
    }
}
