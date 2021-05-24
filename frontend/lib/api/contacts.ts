import axios from "axios";
import { getToken } from "lib/utils/authToken"
import { SERVER_BASE_URL } from "../utils/constant";

const ContactsAPI = {
  all: async (token: string) => {
    try {
      const response = await axios.get(
        `${SERVER_BASE_URL}/contacts`,
        {
          headers: {
            Authorization: `JWT ${token}`,
          },
        }
      );
      return response;
    } catch (error) {
      return error.response;
    }
  },

  delete: (contactId: number, token: string) =>
    axios.delete(`${SERVER_BASE_URL}/contacts/${contactId}/delete`, {
      headers: {
        Authorization: `JWT ${token}`,
      },
    }),

  get: async (contactId: string) => {
    try {
      const token = getToken();
      const response = await axios.get(
        `${SERVER_BASE_URL}/contacts/${contactId}/search`,
        {
          headers: {
            Authorization: `JWT ${token}`,
          },
        }
      );
      return response;
    } catch (error) {
      return error.response;
    }
  },

  update: async (article, token) => {
    const { data, status } = await axios.put(
      `${SERVER_BASE_URL}/articles/${article.slug}`,
      JSON.stringify({ article }),
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${encodeURIComponent(token)}`,
        },
      }
    );
    return {
      data,
      status,
    };
  },

  create: async (contact, token) => {
    const { data, status } = await axios.post(
      `${SERVER_BASE_URL}/contacts`,
      JSON.stringify({ contact }),
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${token}`,
        },
      }
    );
    return {
      data,
      status,
    };
  },
};

export default ContactsAPI;
