SEND_DOCUMENT = """
	<!DOCTYPE html>
		<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width,initial-scale=1">
			<meta name="x-apple-disable-message-reformatting">
			<title></title>
			<!--[if mso]>
			<noscript>
				<xml>
					<o:OfficeDocumentSettings>
						<o:PixelsPerInch>96</o:PixelsPerInch>
					</o:OfficeDocumentSettings>
				</xml>
			</noscript>
			<![endif]-->
			<style>
				table, td, div, h1, p {font-family: Arial, sans-serif;}

				.boton-personalizado-5 {
					margin:0 0 25px 0;
					font-size:16px;
					line-height:24px;
					font-family:Arial,sans-serif;
					text-decoration:none;
					font-weight: 600;
					font-size: 20px;
					color:#ffffff;
					padding-top:15px;
					padding-bottom:15px;
					padding-left:40px;
					padding-right:40px;
					background-color:#f2595e;
					border-color: #F69DA1;
					border-width: 3px;
					border-style: solid;
				}

				.boton-personalizado-6 {
					margin:0 0 25px 0;
					font-size:16px;
					line-height:24px;
					font-family:Arial,sans-serif;
					text-decoration:none;
					font-weight: 600;
					font-size: 20px;
					color:#ffffff;
					padding-top:15px;
					padding-bottom:15px;
					padding-left:40px;
					padding-right:40px;
					background-color:#f2595e;
					border-color: #F69DA1;
					border-width: 3px;
					border-style: solid;
				}


			</style>
		</head>
		<body style="margin:0;padding:0;">
			<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
				<tr>
					<td align="center" style="padding:0;">
						<table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
							<tr>
								<td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
									<img src="https://theriosoft.com/static/home/img/hero-img.png" alt="" width="300" style="height:auto;display:block;" />
								</td>
							</tr>
							<tr>
								<td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
									<img src="letras.png" alt="" width="300" style="height:auto;display:block;">
								</td>
							</tr>
							<tr>
								<td style="padding:36px 30px 42px 30px;">
									<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
										<tr>
											<td style="padding:0 0 36px 0;color:#153643;">
												<p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">
													Hola $(client_name)!. Por medio de la presente, le mandamos los documentos correspondientes a la factura electrónica de venta N° $(invoice_number). Por favor antes de seleccionar alguna de las opciones siguientes, verificar los documentos que se le han adjuntado.
												</p>
											</td>
										</tr>
										<tr>
											<td style="padding:0;">
												<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
													<tr>
														<td style="width:260px;padding:0;vertical-align:top;color:#153643;">
															<a style="text-decoration:none; color:white;" class="boton-personalizado-5" href="http://localhost:8000/api/Send_Thanks/$(invoice_number)/$(pk_company)">ACEPTO</a>
														</td>
														<td style="width:20px;padding:0;font-size:0;line-height:0;">&nbsp;</td>
														<td style="width:260px;padding:0;vertical-align:top;color:#153643;">
															<a style="text-decoration:none; color:white;" class="boton-personalizado-6" href="http://localhost:8000/Rechazo/$(invoice_number)/$(pk_company)">RECHAZO</a>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
							<tr>
								<td style="padding:30px;background:#ee4c50;">
									<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;font-size:9px;font-family:Arial,sans-serif;">
										<tr>
											<td style="padding:0;width:50%;" align="left">
												<p style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
													&reg; 2023<br/><a href="https://theriosoft.com" style="color:#ffffff;text-decoration:underline;">Theriosoft s.a.s</a>
												</p>
											</td>
											<td style="padding:0;width:50%;" align="right">
												<table role="presentation" style="border-collapse:collapse;border:0;border-spacing:0;">
													<tr>
														<td style="padding:0 0 0 10px;width:38px;">
															<a href="https://www.facebook.com/theriosoft.med/" style="color:#ffffff;"><img src="https://assets.codepen.io/210284/fb_1.png" alt="Facebook" width="38" style="height:auto;display:block;border:0;" />
															</a>
														</td>
													</tr>
												</table>
											</td>
										</tr>
									</table>
								</td>
							</tr>
						</table>
					</td>
				</tr>
			</table>
		</body>
	</html>
"""

SEND_THANKS = """
	<!DOCTYPE html>
	<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width,initial-scale=1">
		<meta name="x-apple-disable-message-reformatting">
		<title></title>
		<!--[if mso]>
		<noscript>
			<xml>
				<o:OfficeDocumentSettings>
					<o:PixelsPerInch>96</o:PixelsPerInch>
				</o:OfficeDocumentSettings>
			</xml>
		</noscript>
		<![endif]-->
		<style>
			table, td, div, h1, p {font-family: Arial, sans-serif;}

			.boton-personalizado-5 {
				margin:0 0 25px 0;
				font-size:16px;
				line-height:24px;
				font-family:Arial,sans-serif;
				text-decoration:none;
				font-weight: 600;
				font-size: 20px;
				color:#ffffff;
				padding-top:15px;
				padding-bottom:15px;
				padding-left:40px;
				padding-right:40px;
				background-color:#f2595e;
				border-color: #F69DA1;
				border-width: 3px;
				border-style: solid;
			}

			.boton-personalizado-6 {
				margin:0 0 25px 0;
				font-size:16px;
				line-height:24px;
				font-family:Arial,sans-serif;
				text-decoration:none;
				font-weight: 600;
				font-size: 20px;
				color:#ffffff;
				padding-top:15px;
				padding-bottom:15px;
				padding-left:40px;
				padding-right:40px;
				background-color:#f2595e;
				border-color: #F69DA1;
				border-width: 3px;
				border-style: solid;
			}


		</style>
	</head>
	<body style="margin:0;padding:0;">
		<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;background:#ffffff;">
			<tr>
				<td align="center" style="padding:0;">
					<table role="presentation" style="width:602px;border-collapse:collapse;border:1px solid #cccccc;border-spacing:0;text-align:left;">
						<tr>
							<td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
								<img src="https://theriosoft.com/static/home/img/hero-img.png" alt="" width="300" style="height:auto;display:block;" />
							</td>
						</tr>
						<tr>
							<td align="center" style="padding:40px 0 30px 0;background:#70bbd9;">
								<img src="letras.png" alt="" width="300" style="height:auto;display:block;">
							</td>
						</tr>
						<tr>
							<td style="padding:36px 30px 42px 30px;">
								<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
									<tr>
										<td style="padding:0 0 36px 0;color:#153643;">
											<p style="margin:0 0 12px 0;font-size:16px;line-height:24px;font-family:Arial,sans-serif;">
												Hola $(client_name)!. Gracias por aceptar la factura electrónica de venta N° $(invoice_number). En breves momentos puede ingresar a la DIAN, donde podra obtener el certificado de la factura como titulo valor
												<br>
											</p>
										</td>
									</tr>
								</table>
							</td>
						</tr>
						<tr>
							<td style="padding:36px 30px 42px 30px;">
								<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
									<tr>
										<td style="padding:0;">
											<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;">
												<tr>
													<td style="width:100%;padding:0;vertical-align:top;color:#153643;">
														<a style="text-decoration:none; color:white;" class="boton-personalizado-5" target="_blank" href="https://catalogo-vpfe.dian.gov.co/Document/ShowDocumentToPublic/$(cufe)">IR A LA DIAN</a>
													</td>
												</tr>
											</table>
										</td>
									</tr>
								</table>
							</td>
						</tr>
						<tr>
							<td style="padding:30px;background:#ee4c50;">
								<table role="presentation" style="width:100%;border-collapse:collapse;border:0;border-spacing:0;font-size:9px;font-family:Arial,sans-serif;">
									<tr>
										<td style="padding:0;width:50%;" align="left">
											<p style="margin:0;font-size:14px;line-height:16px;font-family:Arial,sans-serif;color:#ffffff;">
												&reg; 2023<br/><a href="https://theriosoft.com" style="color:#ffffff;text-decoration:underline;">Theriosoft s.a.s</a>
											</p>
										</td>
										<td style="padding:0;width:50%;" align="right">
											<table role="presentation" style="border-collapse:collapse;border:0;border-spacing:0;">
												<tr>
													<td style="padding:0 0 0 10px;width:38px;">
														<a href="https://www.facebook.com/theriosoft.med/" style="color:#ffffff;"><img src="https://assets.codepen.io/210284/fb_1.png" alt="Facebook" width="38" style="height:auto;display:block;border:0;" />
														</a>
													</td>
												</tr>
											</table>
										</td>
									</tr>
								</table>
							</td>
						</tr>
					</table>
				</td>
			</tr>
		</table>
	</body>
	</html>
"""