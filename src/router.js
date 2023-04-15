import { createRouter, createWebHashHistory } from "vue-router";

import admin from "./page/Admin.vue";
import login from "./page/Login.vue";
import edit from "./page/edit.vue";
import create from "./page/create.vue";
import hint from "./page/Hint.vue";
import material from "./page/Material.vue";
import regist from "./page/Regist.vue";
import reserve from "./page/Reserve.vue";
import shopAdmin from "./page/ShopAdmin.vue";
import front from "./page/FrontPage.vue";
import shopUser from "./page/ShopUser.vue";
import shoppingCart from "./page/ShoppingCart.vue";

const routes = [
  { path: "/", component: front },
  { path: "/regist", component: regist },
  { path: "/login", component: login },
  { path: "/shopUser", component: shopUser },
  { path: "/material", component: material },
  { path: "/admin", component: admin },
  { path: "/shopAdmin", component: shopAdmin },
  { path: "/edit", component: edit },
  { path: "/create", component: create },
  { path: "/reserve", component: reserve },
  { path: "/shoppingCart", component: shoppingCart },
  { path: "/hint", component: hint },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
