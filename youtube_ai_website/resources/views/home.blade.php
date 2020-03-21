<!DOCTYPE html>
<html>
<head>
	<title>YVI Generator AI </title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="{{asset('css/app.css')}}">
	<link rel="stylesheet" type="text/css" href="{{asset('css/style.css')}}">
	<link href="https://fonts.googleapis.com/css?family=Montserrat:400,600,900&display=swap" rel="stylesheet">
	<script src="{{asset('js/app.js')}}"></script>
</head>
<body>

	<div class="container-fluid h-100">
		<div class="row h-100 px-lg-5">
			<div class="col-12 my-auto px-lg-5">

				<div class="card">
					<img class="card-img-top" src="{{asset('img/youtubers.jpg')}}" alt="Card image cap">

					<div class="card-body">
						<div class="container-fluid">

							<div class="card-title">
								<h3 class="project_title">YOUTUBE VIDEO IDEA GENERATOR A.I.</h3>
								<p>
									This AI uses Natural Language Processing to generate new YouTube video titles / ideas? 
									It was trained using 20000 video titles collected from some of the most popular YouTube channels. <br>
									<strong>For more AI projects check out</strong> <a href="https://www.youtube.com/channel/UCjOmKLAk8sAw2PKrAERYFaw">this YouTube channel</a> <br>
									<strong>GitHub repo:</strong> <a href="#">www.github.com</a>  
								</p>
							</div>

							<div class="row p-2">
								<div class="col-lg-6 col-12">
									<h5>Type your seed text</h5>
									<div class="row p-0 m-0">
										<input type="text" name="seed" id="seed" class="col-lg-4 col-12 form-control mt-2" placeholder="Type initial text here">
										<button class="col-lg-4 col-12 btn btn-secondary ml-lg-4 mt-2" onclick='generateTitle()'>Generate Video Title</button>
										<!-- <form method="POST" action="/generate">
											@csrf
											<button type="submit">AEL OLE</button>
										</form> -->
									</div>
								</div>
							</div>

							<div class="row pt-4 pb-2 px-2">
								<h5 class="col-12">Titles Generated: </h5>
							</div>

							<div class="row p-2" id="results">

							</div>

						</div>
					</div>
					<div class="card-footer">
						Created by Giorgos Demosthenous
					</div>
				</div>

			</div>
		</div>

	</div>

</body>
</html>

<script type="text/javascript">

	$('#seed').keypress(function (e) {
		if (e.which == 13) {
			generateTitle();
	  		return false;
	  	}
	});
	
	function generateTitle()
	{
		$_seed = $('#seed').val();
		$_token = "{{ csrf_token() }}";
	    $.ajax({
	        headers: { 'X-CSRF-Token' : $('meta[name=_token]').attr('content') },
	        url: "{{ url('/generate') }}",
	        type: 'POST',
	        cache: false,
	        data: {'_token': $_token,'seed':$_seed}, //see the $_token
	        datatype: 'html',
	        beforeSend: function() {
	            $('#results').html('<div class="d-block d-lg-none col-12 text-center"><h5>Generating...</h5><img src="{{asset("img/loading.gif")}}" class="card-img"></div><div class="d-none d-lg-block col-12 "><h5>Generating...</h5><img src="{{asset("img/loading.gif")}}"></div>');
	        },
	        success: function(data) {
	        	console.log(data);
	        	$('#results').html('');
	        	for(var i=0; i< data.length-1; i++)
	        	{
	        		$('#results').append('<div class="col-12"><div class="alert alert-info" role="alert"><h5>'+data[i]+'</h5></div></div>')
	        	}
	        },
	        error: function(xhr,textStatus,thrownError) {
	            alert("Something went wrong. Try again");
	        }
	    });
	}

</script>