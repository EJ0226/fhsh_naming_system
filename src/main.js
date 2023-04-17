import { createApp } from "vue";
import "./style.css";
import APP from "./APP.vue";
import router from "./router";

const app = createAPP(APP);

app.use(router);

app.mount("#app");
