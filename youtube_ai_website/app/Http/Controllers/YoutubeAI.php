<?php

namespace App\Http\Controllers;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;

use Illuminate\Http\Request;

class YoutubeAI extends Controller
{
    
    public function getIndex()
    {
		return view('home');
    }

    public function generateTitle(Request $request)
    {
    	if ($request->seed == null){
    		$text = " ";
    	}else{
    		$text = $request->seed;
    	}

		$process = new Process("python C:/xampp\htdocs/youtube_ai_website/ai_brain/Controller.py \"{$text}\"");
		$process->run();

		// executes after the command finishes
		if (!$process->isSuccessful()) {
		    throw new ProcessFailedException($process);
		}

		$titles = explode("\n", $process->getOutput());

		return $titles;
    }
}
