$(document).ready(function() {
	$(document).on("click", ".share-modal-open", function() {
		var fileKey = $(this).data('id');
		$(".modal-body #share_file_key").val(fileKey);
		$('.modal-body #share-link').attr("href", "/view/" + fileKey);
		$(".modal-body #share-link").html("www.snapfile.biz/view/" + fileKey);
	});
	$(document).on("click", ".del-modal-open", function() {
		var fileKey = $(this).data('id');
		$(".modal-body #delete_file_key").val(fileKey);
		console.log("filekey" + fileKey);
	});
});

