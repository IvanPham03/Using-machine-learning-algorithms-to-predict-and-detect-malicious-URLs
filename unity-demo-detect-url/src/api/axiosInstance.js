import axios from "axios";
const apiUrl_backend_dectect_url = process.env.REACT_APP_API_DETECT_URL

const instance = axios.create({
    baseURL: apiUrl_backend_dectect_url,
    headers: { 'X-Custom-Header': 'foobar' }
});
export default instance