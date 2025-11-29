import { app } from "./firebase.js";
import {
  getAuth,
  GoogleAuthProvider,
  signInWithPopup,
} from "https://www.gstatic.com/firebasejs/11.0.1/firebase-auth.js";

const auth = getAuth(app);
const provider = new GoogleAuthProvider();

export function setupGoogleButton() {
  const googleBtn = document.getElementById("google");

  googleBtn.onclick = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      const token = await result.user.getIdToken();
      const user = result.user;
      localStorage.setItem("authToken", token);
      console.log("Login successful, redirecting...");
      localStorage.setItem("userName", user.displayName);
      localStorage.setItem("userEmail", user.email);
      localStorage.setItem("userPhoto", user.photoURL);

      window.location.href = "QuizzAi/index.html";
    } catch (err) {
      console.error(err);
      alert("Login failed because god hates you");
    }
  };
}
