import AudioUploader from "./components/custom/AudioUploader";
import websiteText from "./assets/websiteText";
import SongAdder from "./components/custom/SongAdder";
import { Separator } from "./components/ui/separator";

function App() {
  return (
    <div className="w-full min-h-screen flex flex-col p-5 justify-between items-center">
      <div className="flex flex-col">
        <h1 className="scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance">
          {websiteText.websiteTitle}
        </h1>
        <p className="text-muted-foreground text-xl">
          {websiteText.websiteSubtitle}
        </p>
      </div>
      <div className="flex flex-col w-full items-center gap-6">
        <AudioUploader />
        <div className="flex items-center w-1/3">
          <Separator />
        </div>
        <SongAdder />
      </div>
      <p className="leading-7 [&:not(:first-child)]:mt-6 text-center">
        {websiteText.creditPart1}{" "}
        <a
          href={websiteText.creditLink1.url}
          target="_blank"
          className="text-primary font-medium underline underline-offset-4"
        >
          {websiteText.creditLink1.text}
        </a>{" "}
        {websiteText.creditPart2}{" "}
        <a
          href={websiteText.creditLink2.url}
          target="_blank"
          className="text-primary font-medium underline underline-offset-4"
        >
          {websiteText.creditLink2.text}
        </a>
      </p>
    </div>
  );
}

export default App;
