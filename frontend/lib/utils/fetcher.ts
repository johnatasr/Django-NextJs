import axios from "axios";

export const updateOptions = () => {
  if (typeof window === "undefined") return {};

  if (!window.localStorage.user) return {};

  if (Object.keys(window.localStorage.user).length === 0) return {};

  const user = JSON.parse(window.localStorage.user);

  if (user.token) {
    return {
      headers: {
        Authorization: `JWT ${user.token}`,
      },
    };
  }
};

export default async function mainFetcher(url) {
  const { data } = await axios.get(url, updateOptions());
  return data;
}
