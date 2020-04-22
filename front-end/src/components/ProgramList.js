import React, { Component } from 'react'

const Programs = ({ programs }) => {

    return (
        <div class="program-header">

            {
                programs.map((program) => (
                    <div class="result-table">
                        <table>
                            <tr>
                                <th>{program.country}</th>
                                <th>{program.name}</th>
                                <th>{program.language}</th>
                                <th>{program.term}</th>
                                <th>{program.areaOfStudy}</th>
                                <th>${program.Cost}</th>
                                <th>{program.Website}</th>
                                <th>Edit</th>
                            </tr>
                        </table>
                    </div>
                ))
            }
        </div>

    )

}

export default Programs;
