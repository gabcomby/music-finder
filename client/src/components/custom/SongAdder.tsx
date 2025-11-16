import websiteText from "@/assets/websiteText";
import { Button } from "../ui/button";

const SongAdder = () => {
  return (
    <div className="flex flex-col w-1/6 gap-4">
      <p className="text-muted-foreground text-sm text-center">
        {websiteText.newSongAdderText}
      </p>
      <Button variant="default">{websiteText.addSongButton}</Button>
    </div>
  );
};

export default SongAdder;
