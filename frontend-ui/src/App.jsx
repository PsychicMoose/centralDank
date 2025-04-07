import { useEffect, useState } from "react"
import { motion, AnimatePresence } from "framer-motion"
import "@fontsource/inter"                // for "hello" and "DANIEL"
import "@fontsource/space-grotesk"
import "@fontsource/lexend-deca"
import "@fontsource/rubik-mono-one"

const phrases = [
  { word: "builder" },
  { word: "explorer" },
  { word: "hero" },
  { word: "DANIEL" }
]

export default function App() {
  const [index, setIndex] = useState(0)
  const [password, setPassword] = useState("")
  const [isLoggedIn, setIsLoggedIn] = useState(() => {
    const saved = localStorage.getItem("loginTime")
    if (!saved) return false

    const loginTime = parseInt(saved)
    const now = Date.now()
    const hoursSince = (now - loginTime) / (1000 * 60 * 60)

    return hoursSince < 1
  })
  const [error, setError] = useState("")

  const getFontFamily = (word) => {
    switch (word) {
      case "builder":
        return '"Space Grotesk", sans-serif'
      case "explorer":
        return '"Lexend Deca", sans-serif'
      case "hero":
        return '"Rubik Mono One", sans-serif'
      case "DANIEL":
        return '"Inter", sans-serif'
      default:
        return 'sans-serif'
    }
  }

  const handleLogin = async () => {
    const res = await fetch("http://localhost:8000/api/verify-password/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password }),
    })

    if (res.ok) {
      setIsLoggedIn(true)
      setIndex(0)
      localStorage.setItem("loginTime", Date.now().toString())
      setError("")
    } else {
      setError("Access denied.")
    }
  }

  useEffect(() => {
    if (!isLoggedIn) return
    if (index < phrases.length - 1) {
      const timeout = setTimeout(() => {
        setIndex((prev) => prev + 1)
      }, 2000)
      return () => clearTimeout(timeout)
    }
  }, [index, isLoggedIn])

  if (!isLoggedIn) {
    return (
      <div className="h-screen flex flex-col items-center justify-center bg-black text-white">
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleLogin()}
          className="bg-transparent border-b border-white text-center text-xl focus:outline-none mb-4"
        />
        <button
          onClick={handleLogin}
          className="border border-white px-4 py-2 text-white hover:bg-white hover:text-black transition"
        >
          Enter
        </button>
        {error && <p className="mt-4 text-red-500">{error}</p>}
      </div>
    )
  }

  return (
    <div className="h-screen bg-black text-white font-inter relative">
      <button
        onClick={() => {
          localStorage.removeItem("loginTime")
          setIsLoggedIn(false)
          setIndex(0)
          window.location.reload()
        }}
        className="absolute top-4 right-4 text-sm text-white underline"
      >
        Logout
      </button>

      <div className="h-full flex items-center justify-center">
        <div className="text-5xl flex gap-4">
          <span>hello&nbsp;</span>
          <AnimatePresence mode="wait">
            <motion.span
              key={phrases[index].word}
              style={{ fontFamily: getFontFamily(phrases[index].word) }}
              className="text-white"
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.5 }}
            >
              {phrases[index].word}
            </motion.span>
          </AnimatePresence>
        </div>
      </div>
    </div>
  )
}
