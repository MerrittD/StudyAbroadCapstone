import React from 'react'
import NavBar from '../components/NavBar'
import ProgramList from '../components/ProgramList'

export default function AdminDashboard() {
    return (
        <div>
            <button className="large-button">Add Program</button>
            <button className="large-button">Edit Program</button>
            <button className="large-button">Delete Program</button>
            <ProgramList />
        </div>
    )
}
