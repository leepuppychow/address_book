import Vue from 'vue';

const baseUrl = 'http://localhost:5000/api/v1';
const headers = {
  'Content-Type': 'application/json',
};

export const login = body => Vue.http.post(`${baseUrl}/login`, body, headers);
export const register = body => Vue.http.post(`${baseUrl}/register`, body, headers);
