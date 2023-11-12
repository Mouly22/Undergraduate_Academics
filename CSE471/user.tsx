// user.tsx

import React, { useState } from "react";

// Define the user data type
export interface UserData {
  userid: string;
  password: string;
  email: string;
  address: string;
  nid: number;
  user_type: string;
}

export const UserCard: React.FC<{
  userData: UserData;
  setUserData: React.Dispatch<React.SetStateAction<UserData>>;
}> = ({ userData, setUserData }) => {
  const [isEditing, setIsEditing] = useState(false);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUserData({
      ...userData,
      [event.target.name]: event.target.value,
    });
  };

  return (
    <div className="container">
      {!isEditing ? (
        <div className="d-flex justify-content-center">
          <div className="container" style={{ maxWidth: "500px" }}>
            <div className="card mx-5">
              <div className="card-body">
                <h1 className="card-title text-center mt-3 mb-3">
                  User Profile
                </h1>
                <p className="card-text">
                  <b>Role :</b>{" "}
                  <p className="alert alert-success " role="alert">
                    {userData.user_type}
                  </p>
                  <b>User ID:</b>
                  <p className="alert alert-success " role="alert">
                    {" "}
                    {userData.userid}
                  </p>
                  <b>Email:</b>{" "}
                  <p className="alert alert-success" role="alert">
                    {userData.email}
                  </p>
                  <b>Address:</b>
                  <p className="alert alert-success" role="alert">
                    {" "}
                    {userData.address}
                  </p>
                  <b>NID:</b>{" "}
                  <p className="alert alert-success" role="alert">
                    {userData.nid}
                  </p>
                </p>
              <div className="d-flex justify-content-center">
                <button
                  type="button"
                  className="btn btn-primary"
                  onClick={() => setIsEditing(true)}
                >
                  Edit
                </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      ) : (
<div className="card mx-auto" style={{ maxWidth: '500px' }}>
  <div className="card-body">
    <h1 className="card-title text-center mt-3 mb-3">
      Edit User Profile
    </h1>
    <form>
      <div className="card-text w-100">
        <label className="form-label w-100">
          <b>User ID:</b>
          <input
            type="text"
            name="userid"
            className="form-control"
            value={userData.userid}
            onChange={handleInputChange}
          />
        </label>
        <br />
      </div>

      <div className="mb-2 w-100">
        <label className="form-label w-100">
          <b>Email:</b>
          <input
            type="text"
            name="email"
            className="form-control"
            value={userData.email}
            onChange={handleInputChange}
          />
        </label>
        <br /></div>
        <div className="mb-2 w-100">
  <label className="form-label w-100">
    <b>Address:</b>
    <input
      type="text"
      name="address"
      className="form-control"
      value={userData.address}
      onChange={handleInputChange}
    />
  </label>
  <br />
</div>

<div className="mb-2 w-100">
  <label className="form-label w-100">
    <b>NID:</b>
    <input
      type="number"
      name="nid"
      className="form-control"
      value={userData.nid}
      onChange={handleInputChange}
    />
  </label>
  <br />
</div>


              <div className="d-flex justify-content-center">
  <button
    type="button"
    className="btn btn-success"
    onClick={() => setIsEditing(false)}
  >
    Save
  </button>
</div>

            </form>
          </div>
        </div>
      )}
    </div>
  );
};
