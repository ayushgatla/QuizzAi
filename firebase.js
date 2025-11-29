import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyDS_PlPpetjsZXYw_Kmacbd_T-ssV8bVfk",
  authDomain: "quizzai-8117.firebaseapp.com",
  projectId: "quizzai-8117",
  storageBucket: "quizzai-8117.firebasestorage.app",
  messagingSenderId: "638700346942",
  appId: "1:638700346942:web:213044358ff3ac24183b6f",
  measurementId: "G-262SN16RVR",
};

export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
