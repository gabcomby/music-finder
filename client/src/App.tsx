import AudioUploader from "./components/custom/AudioUploader";

function App() {
  return (
    <div className="w-full min-h-screen flex flex-col p-5 justify-between items-center">
      <div className="flex flex-col">
        <h1 className="scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance">
          Music Finder
        </h1>
        <p className="text-muted-foreground text-xl">
          A simple recreation of Shazam using Python.
        </p>
      </div>
      <AudioUploader />
      <p className="leading-7 [&:not(:first-child)]:mt-6 text-center">
        Made with ❤️ by{" "}
        <a
          href="https://github.com/gabcomby"
          target="_blank"
          className="text-primary font-medium underline underline-offset-4"
        >
          @gabcomby
        </a>{" "}
        using the{" "}
        <a
          href="https://michaelstrauss.dev/shazam-in-python"
          target="_blank"
          className="text-primary font-medium underline underline-offset-4"
        >
          incredible work of Michael Strauss.
        </a>
      </p>
    </div>
  );
}

export default App;
