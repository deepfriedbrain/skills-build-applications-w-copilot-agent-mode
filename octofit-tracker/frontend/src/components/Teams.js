import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `${process.env.REACT_APP_CODESPACE_URL}/api/teams/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Teams endpoint:', endpoint);
        console.log('Fetched teams:', results);
      });
  }, [endpoint]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="heading">Teams</h2>
        <table className="table table-striped table-bordered">
          <thead className="thead-dark">
            <tr>
              <th>Name</th>
              <th>Members</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team, idx) => (
              <tr key={idx}>
                <td>{team.name}</td>
                <td>{Array.isArray(team.members)
                  ? team.members.join(', ')
                  : typeof team.members === 'string'
                    ? team.members.replace(/\[|\]|'/g, '').split(',').map(m => m.trim()).join(', ')
                    : ''}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Teams;
