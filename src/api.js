import axios from "axios";

const request = axios.create({
  baseURL: "http://localhost:8000/create_item",
});

export const uploadProd = (data) => {
  request.post("/create_item", data).then(() => {
    alert("上架成功！");
  });
};
