import { SERVER_BASE_URL } from "lib/utils/constant";
import axios from "axios";
import { mutate } from "swr";


const getUserInStorange = () => {
    if (typeof window === "undefined") return {};
  
    if (!window.localStorage.user) return {};
  
    if (Object.keys(window.localStorage.user).length === 0) return {};
  
    const user = JSON.parse(window.localStorage.user);
  
    if (user) {
      return user
    }

    return false
}


export const getToken = () => {
    const user = getUserInStorange()
    return user.tokenAccess
};


export async function resetUserToken() {
    const user = getUserInStorange()
    
    if (user) {
        const response = await axios.get(SERVER_BASE_URL+`/auth/token/refresh/`, {
            headers: {
              Authorization: `Token ${user.refreshToken}`,
            }
        })

        if (response.data) {
            let data = response.data;

            const user = JSON.parse(window.localStorage.user)
            window.localStorage.setItem("user", JSON.stringify({ tokenAcess: user.tokenAcess, refreshToken: data.refresh, username: user.username }));
            mutate("user", data);
          }
        return response;
    }
}
  