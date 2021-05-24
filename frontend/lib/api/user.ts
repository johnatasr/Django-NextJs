import axios from "axios";

import { SERVER_BASE_URL } from "../utils/constant";

const UserAPI = {
  current: async () => {
    const user: any = window.localStorage.getItem("user");
    const token = user?.token;
    try {
      const response = await axios.get(`/user`, {
        headers: {
          Authorization: `Token ${encodeURIComponent(token)}`,
        },
      });
      return response;
    } catch (error) {
      return error.response;
    }
  },
  login: async (email: string, password: string) => {
    try {
      const response = await axios.post(
        `${SERVER_BASE_URL}/auth/token/obtain/`,
        JSON.stringify({ username: email, password: password }),
        {
          headers: {
            'Accept': 'application/json',
            "Content-Type": "application/json",
          },
        }
      );
      return response;
    } catch (error) {
      return error.response;
    }
  },
  register: async (username: string, email: string, password: string) => {
    try {
      const response = await axios.post(
        `${SERVER_BASE_URL}/auth/user/create/`,
        JSON.stringify({ email: email, username: username, password: password }),
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      return response;
    } catch (error) {
      return error.response;
    }
  },

};

export default UserAPI;
